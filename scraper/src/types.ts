import {
  PopularScraper,
  BanreservasScraper,
  BHDScraper,
  ScotiabankScraper,
} from "src/scrapers";
import { BROWSER_NAME } from "src/enums";

export type SimpleScrapers = any[];
export type BrowserScrapers = (
  | typeof PopularScraper
  | typeof BanreservasScraper
  | typeof BHDScraper
  | typeof ScotiabankScraper
)[];
export type BrowserScrapersClasses = {
  [key in BROWSER_NAME]: BrowserScrapers;
};
