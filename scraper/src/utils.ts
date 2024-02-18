export function validateAmount(
  target: any,
  key: string,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value;

  descriptor.value = async function (...args: any[]) {
    try {
      const amount: number = await originalMethod.apply(this, args);
      if (isNaN(amount) || !isFinite(amount)) {
        throw Error(`Invalid number: ${amount}`);
      }

      return amount;
    } catch (err) {
      console.error(`Outdated selector for ${key}`);
      throw err;
    }
  };

  return descriptor;
}
