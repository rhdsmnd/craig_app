package com.rhd.craig_app.services;

import com.rhd.craig_app.domain.Listing;

public interface ListingsService {

    public Listing[] getListings();
    public Listing[] getListings(Long ts);
}