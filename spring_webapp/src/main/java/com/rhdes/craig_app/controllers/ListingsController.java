package com.rhd.craig_app.controllers;

import com.rhd.craig_app.domain.Listing;

import com.rhd.craig_app.services.ListingsService;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
public class ListingsController {



    private ListingsService listingsService;

    @RequestMapping("/listings")
    public Listing[] getListings(@RequestParam(value="startTs", required=false, defaultValue="0") String startTs) {
        Long parsedStartTs;
        try {
            parsedStartTs = Long.parseLong(startTs);
        } catch (NumberFormatException e) {
            return null;
        }
        if (parsedStartTs < 0) {
            return null;
        }

        Listing[] ret = listingsService.getListings();

        return ret;
    }

    public ListingsService getListingsService() {
        return listingsService;
    }

    @Autowired
    public void setListingsService(ListingsService listingsService) {
        this.listingsService = listingsService;
    }

}