CODECOV_TOKEN="835a4597-5614-40f5-803c-093464aa2a74"


idpolicies=$(curl -X GET 'https://api.newrelic.com/v2/alerts_policies.json' -H X-Api-Key: b862dec293faae411c31b3160819c591 -s -G |jq '.policies[] .id')

apikey: b862dec293faae411c31b3160819c591
