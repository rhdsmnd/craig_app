package com.rhd.craig_app.services;

public interface ListingsService {

    public Listings[] getListings() {
        return getListings(10);
    }

    public Listings[] getListings(int num);
}