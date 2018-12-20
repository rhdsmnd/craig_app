package com.rhd.craig_app.dao;

import com.rhd.craig_app.domain.Listing;

public interface ListingsDAO {

    public Listing[] queryDb(Long ts);
}