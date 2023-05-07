// This function calculates (base ^ exp) % mod
export function expmod(base: bigint, exp: bigint, mod: bigint): bigint {
  if (exp == 0n) return 1n;
  if (exp % 2n == 0n) {
    return expmod(base, exp / 2n, mod) ** 2n % mod;
  } else {
    return (base * expmod(base, exp - 1n, mod)) % mod;
  }
}

export async function randomNBitPrime(n: number) {
  const resp = await fetch(import.meta.env.VITE_PRIME_URL + "/" + n);
  return BigInt(await resp.text());
}

export function bufToBigInt(arr: Uint8Array) {
  arr = arr.reverse();
  let result = BigInt(0);
  for (let i = 0; i < arr.length; i++) {
    result = result * BigInt(256) + BigInt(arr[i]);
  }
  return result;
}

export function bigIntTobuf(num: bigint) {
  let result = new Uint8Array(200);
  let i = 0;
  while (num > 0n) {
    result[i] = Number(num % 256n);
    num = num / 256n;
    i += 1;
  }
  return result.subarray(0, i);
}

export function encryptMessage(message: string, pubkey: bigint) {
  const encoder = new TextEncoder();
  let cipher = bufToBigInt(encoder.encode(message));
  let c = expmod(cipher, 0x10001n, pubkey);
  return c;
}

export function decryptMessage(c: bigint, privkey: bigint, pubkey: bigint) {
  const cNum = expmod(c, privkey, pubkey);
  const cipher = bigIntTobuf(cNum);
  const decoder = new TextDecoder();
  return decoder.decode(cipher);
}

export function modInverse(a: bigint, m: bigint) {
  // Extended Euclidian algorithm
  //   https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
  //   https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
  var oldR = a;
  var r = m;
  var oldS = 1n;
  var s = 0n;

  while (r > 0n) {
    // BigInt division truncates, which is what we want.
    var quot = oldR / r;

    var tempR = r;
    r = oldR - quot * r; // alternatively, r = oldR % r;
    oldR = tempR;

    var tempS = s;
    s = oldS - quot * s;
    oldS = tempS;
  }

  if (oldS < 0) oldS += m;
  return oldS;
}
