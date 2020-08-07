module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  pages: {
    index: {
      entry: "src/main.js",
      title: "TimeIsMoney",
    },
  },
  pwa: {
    name: "time-is-money",
    manifestPath: "static/manifest.json",
    manifestOptions: {
      icons: [
        {
          src: "img/icons/android-chrome-192x192.png",
          sizes: "192x192",
          type: "image/png",
        },
        {
          src: "img/icons/android-chrome-512x512.png",
          sizes: "512x512",
          type: "image/png",
        },
      ],
    },
    outputDir: "static",
    iconPaths: {
      favicon: "static/favicon.ico",
      favicon32: "static/favicon.ico",
      favicon16: "static/favicon.ico",
      appleTouchIcon: "static/img/icons/apple-touch-icon-152x152.png",
      maskIcon: "static/img/icons/safari-pinned-tab.svg",
      msTileImage: "static/img/icons/msapplication-icon-144x144.png",
    },
    workboxPluginMode: "GenerateSW",
    workboxOptions: {
      swDest: "static/service-worker.js",
      // ...other Workbox options...
      importsDirectory: "static",
    },
  },
};
