(not (or  
    (and (== (userHasRole01 (?o) "executive") 1) (== (userHasRole01 (?o) "judicial") 1))
    (and (== (userHasRole01 (?o) "executive") 1) (== (userHasRole01 (?o) "legislator") 1))
    (and (== (userHasRole01 (?o) "judicial") 1) (== (userHasRole01 (?o) "legislator") 1))
))
