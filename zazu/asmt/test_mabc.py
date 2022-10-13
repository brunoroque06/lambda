from datetime import date

from asmt import mabc


def test_mabc_6():
    raw = {
        "hg11": 17,
        "hg12": 29,
        "hg2": 32,
        "hg3": 0,
        "bf1": 4,
        "bf2": 0,
        "bl11": 9,
        "bl12": 7,
        "bl2": 20,
        "bl3": 1,
    }

    comp, agg = mabc.process(date(2016, 1, 1), date(2022, 1, 2), raw)

    comp_res = [
        ["bf1", 5],
        ["bf2", 1],
        ["bl1", 7],
        ["bl11", 6],
        ["bl12", 8],
        ["bl2", 11],
        ["bl3", 1],
        ["hg1", 6],
        ["hg11", 11],
        ["hg12", 1],
        ["hg2", 14],
        ["hg3", 11],
    ]

    for k, v in comp_res:
        assert comp.loc[k].standard == v

    agg_res = [
        ["bf", 1],
        ["bl", 6],
        ["hg", 11],
        ["total", 5],
    ]

    for k, v in agg_res:
        assert agg.loc[k].standard == v


def test_mabc_9():
    raw = {
        "hg11": 28,
        "hg12": 25,
        "hg2": 25,
        "hg3": 1,
        "bf1": 9,
        "bf2": 7,
        "bl11": 30,
        "bl12": 9,
        "bl2": 7,
        "bl31": 5,
        "bl32": 4,
    }

    comp, agg = mabc.process(date(2013, 1, 1), date(2022, 1, 2), raw)

    comp_res = [
        ["bf1", 12],
        ["bf2", 11],
        ["bl1", 12],
        ["bl11", 13],
        ["bl12", 10],
        ["bl2", 1],
        ["bl3", 8],
        ["bl31", 11],
        ["bl32", 6],
        ["hg1", 11],
        ["hg11", 8],
        ["hg12", 14],
        ["hg2", 9],
        ["hg3", 6],
    ]

    for k, v in comp_res:
        assert comp.loc[k].standard == v

    agg_res = [
        ["bf", 12],
        ["bl", 6],
        ["hg", 9],
        ["total", 8],
    ]

    for k, v in agg_res:
        assert agg.loc[k].standard == v