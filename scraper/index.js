import puppeteer from "puppeteer";

export const handler = async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    timeout: 3000,
    args: ["--no-sandbox"],
  });
  const page = await browser.newPage();

  await page.goto("https://popularenlinea.com/personas/Paginas/Home.aspx");
  const euroBuyElement = await page.waitForSelector(
    "#compra_peso_euro_desktop"
  );
  const value = await euroBuyElement.evaluate((el) => el.value);
  console.log(`Buy euro rate ${value}`);

  await browser.close();
};

handler();
