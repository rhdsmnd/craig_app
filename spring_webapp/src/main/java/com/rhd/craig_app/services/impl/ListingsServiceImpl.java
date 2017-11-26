package com.rhd.craig_app.services.impl;

import rhd.craig_app.services.ListingsService;
import rhd.craig_app.dao.ListingsDAO;
import rhd.craig_app.domain.Listing;

import org.springframework.beans.factory.annotation.Autowired;

public class ListingsServiceImpl implements ListingsService {

    private ListingsDAO listingsDAO;

    public Listing[] getListings() {
        return getListings(10);
    }

    public Listing[] getListings(int num) {
        // connect to database
        // retrieve & return 20 most recent posts

        Listing[] listingsRes = listingsDAO.queryDb(num);

        return listingsRes;
    }

    @Autowired
    public void setListingsDAO(ListingsDAO listingsDAO) {
        this.listingsDAO = listingsDAO;
    }

    public ListingsDAO getListingsDAO() {
        return this.listingsDAO;
    }
}