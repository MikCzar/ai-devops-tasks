const ipv4Regex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

function isValidIPv4(ip) {
  return ipv4Regex.test(ip);
}

console.log(isValidIPv4("192.168.1.1")); // true
console.log(isValidIPv4("256.100.0.1")); // false (256 jest poza zakresem)
console.log(isValidIPv4("10.0.0"));      // false (brak czwartego oktetu)