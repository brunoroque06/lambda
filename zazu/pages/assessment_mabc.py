import datetime

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import mabc


@st.cache()
def load():
    return mabc.load()


with st.sidebar:
    col1, col2 = st.columns(2)

    today = datetime.date.today()
    birth = col1.date_input(
        "Birthday",
        today - relativedelta(years=6),
        max_value=today - relativedelta(years=6),
    )
    asmt = col2.date_input("Assessment", today, max_value=today)

    age = mabc.get_age(birth, asmt)
    st.text(f"Age: {age.years} years, {age.months} months, {age.days} days")

st.header("M ABC")

vld, err = mabc.valid_age(birth, asmt)
if not vld:
    st.error(err)
    st.stop()

form = st.form(key="results")
comps = mabc.get_comps(birth, asmt)
comp_ids = list(comps.keys())
cols = form.columns(len(comp_ids))

raw = {}

for i, col in enumerate(cols):
    comp_id = comp_ids[i]
    col.markdown(f"***{comp_id}***")
    for exe in comps[comp_id]:
        raw[exe] = col.number_input(
            label=exe.upper(), min_value=0, max_value=100, step=1
        )

submit = form.form_submit_button("Submit")

if submit:
    with st.spinner("Processing..."):
        comp, agg = mabc.process(birth, asmt, raw)

    def color_rank(row):
        rank = row["rank"]
        if pd.isna(rank):
            color = None
        elif rank == 0:
            color = "rgba(40, 167, 69, 0.1)"
        elif rank == 1:
            color = "rgba(255, 193, 7, 0.1)"
        else:
            color = "#ffe6e6"

        if color is None:
            return [""] * len(row)
        return [f"background-color: {color}"] * len(row)

    st.subheader("Component Results")
    # df.style.hide() is not supported at the moment
    st.table(comp.style.apply(color_rank, axis=1))
    st.subheader("Aggregated Results")
    st.table(agg.style.apply(color_rank, axis=1).format({"percentile": "{:.1f}"}))
    st.balloons()