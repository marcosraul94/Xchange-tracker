import { environment } from "src/env";
import { ScrapingSession } from "src/app";
import {
  PopularScraper,
  BanreservasScraper,
  ScotiabankScraper,
  BHDScraper,
  ApapScraper,
  BanescoScraper,
  PromericaScraper,
} from "src/scrapers";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const scrapingSession = new ScrapingSession({
    timeout: 10000,
    Scrapers: [
      BanescoScraper,
      ScotiabankScraper,
      PopularScraper,
      BanreservasScraper,
      ApapScraper,
      PromericaScraper,
      BHDScraper,
    ],
  });

  await scrapingSession.run();
  await scrapingSession.save();

  console.log(scrapingSession.results);
};

handler();
