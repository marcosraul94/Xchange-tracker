export function validateAmount(
  target: any,
  key: string,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value;
  const methodName = key;
  const className = target.constructor.name;

  descriptor.value = async function (...args: any[]) {
    try {
      const amount: number = await originalMethod.apply(this, args);
      if (isNaN(amount) || !isFinite(amount)) {
        throw Error(`Invalid number: ${amount}`);
      }

      return amount;
    } catch (err) {
      console.error(`Outdated selector for ${methodName} from ${className}`);
      throw err;
    }
  };

  return descriptor;
}

export const delay = (delayInms: number) => {
  return new Promise((resolve) => setTimeout(resolve, delayInms));
};

export class NotImplementedError extends Error {
  constructor(message?: string) {
    super(message || 'This method or functionality is not implemented.');
    this.name = 'NotImplementedError';
  }
}