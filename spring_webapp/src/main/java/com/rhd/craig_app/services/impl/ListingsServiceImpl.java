package com.rhd.craig_app.services.impl;

import com.rhd.craig_app.services.ListingsService;
import com.rhd.craig_app.dao.ListingsDAO;
import com.rhd.craig_app.domain.Listing;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

@Service
public class ListingsServiceImpl implements ListingsService {

    private ListingsDAO listingsDAO;

    public Listing[] getListings() {
        return getListings(0);
    }

    public Listing[] getListings(Long ts) {
        // connect to database
        // retrieve & return 20 most recent posts

        Listing[] listingsRes = listingsDAO.queryDb(ts);

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