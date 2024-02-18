import { environment } from "./src/env";

export const handler = async () => {
  console.log(`Running lambda in ${environment} environment.`);
};
