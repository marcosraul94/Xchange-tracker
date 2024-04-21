import { environment } from "src/env";
import { ScrapingSession } from "src/app";
import {
  PopularScraper,
  BanreservasScraper,
  ScotiabankScraper,
  BHDScraper,
} from "src/scrapers";
import { BROWSER_NAME } from "src/enums";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const scrapingSession = new ScrapingSession({
    timeout: 10000,
    browserScrapersClasses: {
      [BROWSER_NAME.FIREFOX]: [ScotiabankScraper, PopularScraper, BanreservasScraper],
      [BROWSER_NAME.CHROME]: [BHDScraper],
    },
    simpleScraperClasses: [],
  });

  await scrapingSession.run();
};

handler();
