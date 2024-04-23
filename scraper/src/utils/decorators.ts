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

export function time(target: any, key: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;

  descriptor.value = async function (...args: any[]) {
    const now = new Date();
    const result = await originalMethod.apply(this, args);

    const after = new Date();
    const seconds = ((after.getTime() - now.getTime()) / 1000).toFixed(2);
    console.log(`Time: ${seconds}s`);

    return result;
  };

  return descriptor;
}
