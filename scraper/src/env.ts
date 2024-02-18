import { ENVIRONMENT } from "./enums";

export const environment = process.env["ENVIRONMENT"] || ENVIRONMENT.TEST;
