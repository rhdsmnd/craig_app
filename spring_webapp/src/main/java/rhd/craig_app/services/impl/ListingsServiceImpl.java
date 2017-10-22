package com.rhd.craig_app.services.impl;

import com.rhd.craig_app.services.ListingsService;

public class ListingsServiceImpl implements ListingsService {

    public Listings[] getListings() {
        return getListings(10);
    }

    public Listings[] getListings(int num) {
        // connect to database
        // retrieve & return 20 most recent posts
        return new Listings[1];
    }
}