import { PopularScraper, BanreservasScraper } from "src/scrapers";

export type SimpleScrapers = any[];
export type BrowserScrapers = (
  | typeof PopularScraper
  | typeof BanreservasScraper
)[];
