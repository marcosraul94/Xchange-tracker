import { environment } from "src/env";
import { ScrapingSession } from "src/app";
import {
  PopularScraper,
  BanreservasScraper,
  ScotiabankScraper,
  BHDScraper,
} from "src/scrapers";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const scrapingSession = new ScrapingSession({
    timeout: 10000,
    concurrency: 1,
    browserScraperClasses: [
      PopularScraper,
      BanreservasScraper,
      ScotiabankScraper,
      BHDScraper,
    ],
    simpleScraperClasses: [],
  });

  await scrapingSession.run();
};

handler();
