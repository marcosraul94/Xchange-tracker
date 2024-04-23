export class NotImplementedError extends Error {
  constructor(message?: string) {
    super(message || "This method or functionality is not implemented.");
    this.name = "NotImplementedError";
  }
}
