import { environment } from "src/env";
import { ScrapingSession } from "src/app";
import {
  PopularScraper,
  BanreservasScraper,
  ScotiabankScraper,
  BHDScraper,
  ApapScraper,
  BanescoScraper,
} from "src/scrapers";
import { BROWSER_NAME } from "src/enums";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);

  const scrapingSession = new ScrapingSession({
    timeout: 10000,
    browserScrapersClasses: {
      [BROWSER_NAME.FIREFOX]: [
        BanescoScraper,
        ScotiabankScraper,
        PopularScraper,
        BanreservasScraper,
      ],
      [BROWSER_NAME.CHROME]: [BHDScraper, ApapScraper],
    },
    simpleScraperClasses: [],
  });

  await scrapingSession.run();
};

handler();
