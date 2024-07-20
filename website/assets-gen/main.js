let fs = require("fs");
let sharp = require("sharp");

const imgs = "src/assets/imgs";

/**
 * @returns {Promise<void>}
 */
async function buildFavicons() {
  let svg = sharp("assets-gen/logo.svg");
  await svg.resize(192).png().toFile(`${imgs}/favicon-192.png`);
}

[imgs].forEach((d) => {
  if (!fs.existsSync(d)) {
    fs.mkdirSync(d, { recursive: true });
  }
});

buildFavicons().catch((e) => console.error(e));
