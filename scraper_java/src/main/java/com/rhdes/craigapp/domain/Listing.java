package com.rhdes.craigapp.domain;

import java.math.BigDecimal;
import java.util.Date;


public class Listing {
    private String title;
    private Date date;
    private double price;
    private int bedrooms;
    private String neighborhood;
    private Location loc;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getBedrooms() {
        return bedrooms;
    }

    public void setBedrooms(int bedrooms) {
        this.bedrooms = bedrooms;
    }

    public String getNeighborhood() {
        return neighborhood;
    }

    public void setNeighborhood(String neighborhood) {
        this.neighborhood = neighborhood;
    }

    public Location getLoc() {
        return loc;
    }

    public void setLoc(Location loc) {
        this.loc = loc;
    }

    @Override
    public String toString() {
        return "{\n"
                + "    title: \"" + this.title + "\""
                + "    date: " + this.date
                + "    price: " + this.price
                + "    bedrooms: " + this.bedrooms
                + "    location: " + this.loc
                + "\n}";
    }
}
