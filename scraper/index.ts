import { environment } from "src/env";
import { PopularScraper } from "src/scrapers/popular";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const popularScraper = new PopularScraper();
  const result = await popularScraper.scrape();
  console.log(result);
};

handler();
