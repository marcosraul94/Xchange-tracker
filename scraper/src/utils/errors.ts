export class NotImplementedError extends Error {
  constructor(message?: string) {
    super(message || "This method or functionality is not implemented.");
    this.name = "NotImplementedError";
  }
}

export class InvalidAmountError extends Error {
  constructor(amount: any) {
    super(`Invalid number: ${amount}`);
    this.name = "InvalidAmountError";
  }
}
