import { environment } from "src/env";
import { ScrapingSession } from "src/app";
import { PopularScraper } from "src/scrapers/popular";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const scrapingSession = new ScrapingSession({
    concurrency: 1,
    browserScraperClasses: [PopularScraper],
    simpleScraperClasses: [],
  });

  await scrapingSession.run();
};

handler();
