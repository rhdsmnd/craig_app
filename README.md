# Apartment Finder

### The Interface (broadly speaking)

Everyone who is looking for an apartment to rent has at least two primary goals:

 - have it be in an area where they want to live in
 - have a desired price it should be at or under
 
A problem is that most apartment listing services do not fulfill the first at a fine granularity (i.e. "this 5-block region within a city", not merely "this city").
 
 
A second problem is that fulfilling these goals are more-or-less a zero-sum game -- when a 'high-value' listing (price, location, ane perhaps good 'intangibles' like clear photos and a well-written summary) comes on the market, when one person wins the lease everyone else who wants to rent it loses.  An argument, from which source I've forgotten, which I agree with and still hold is that since landlords or building managers mainly care about filling the spot the fastest with someone meeting a more-or-less standard threshold (proof of income, credit rating, and references). The key, then, to maximizing your chances of locking down a lease for a 'high-value' listing is to be the first qualified candidate to contact the landlord and complete the process for securing a lease.  In essence, it is a market inefficiency, and the first entity (person or group of people who want to live together) to discover and act on it wins.


As programmers, we can use computers -- who are much better at the mindless task of checking whether a new listing is posted and doing rudimentary analysis on its data such as location & price -- to do our bidding for us, those wonderful creations.  They can check at regular intervals and notify us when a listing with qualities that we find desirable has been put on the market.


### The Implementation
