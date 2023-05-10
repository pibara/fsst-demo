(not
  (or  
    (and 
      (== 
        (userHasRole
          (get (?o) "_user/username")
          "executive"
        )
        1
      ) 
      (== 
        (userHasRole 
          (get (?o) "_user/username") 
          "judicial"
        )
        1
      )
    )
    (and 
      (== 
        (userHasRole
          (get (?o) "_user/username")
          "executive"
        )
        1
      ) 
      (==
        (userHasRole
          (get (?o) "_user/username")
          "legislator"
        )
        1
      )
    )
    (and 
      (==
        (userHasRole
          (get (?o) "_user/username")
          "judicial"
        )
        1
      ) 
      (== 
        (userHasRole
          (get (?o) "_user/username")
          "legislator"
        )
        1
      )
    )
  )
)
