const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true
})

// const os = require('os');
// function gethostip() {
//   var interfaces = os.networkInterfaces();
//   for (var devName in interfaces) {
//     var iface = interfaces[devName];
//     for (var i = 0; i < iface.lenght; i++) {
//       var alias = iface[i];
//       if (
//         alias.family === "IPv4" &&
//         alias.address !== "127.0.0.1" &&
//         !alias.internal
//       ) {
//         console.log(alias.address);
//       }
//     }
//   }
// }
