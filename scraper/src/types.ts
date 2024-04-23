import { BrowserScraper } from "src/scrapers";
import { BROWSER_NAME } from "src/enums";

export type SimpleScrapers = any[];
export type BrowserScrapersClasses = {
  [key in BROWSER_NAME]?: (typeof BrowserScraper)[];
};
