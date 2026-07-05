self.__BUILD_MANIFEST = {
  "__rewrites": {
    "afterFiles": [
      {
        "source": "/settings/tab/profile",
        "destination": "/settings"
      },
      {
        "source": "/settings/tab/:tab",
        "destination": "/settings?tab=:tab"
      }
    ],
    "beforeFiles": [],
    "fallback": []
  },
  "sortedPages": [
    "/_app",
    "/_error"
  ]
};self.__BUILD_MANIFEST_CB && self.__BUILD_MANIFEST_CB()