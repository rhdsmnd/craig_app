package com.rhdes.craigapp;

import com.rhdes.craigapp.domain.Listing;
import com.rhdes.craigapp.domain.ScraperConfig;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;

import java.io.IOException;
import java.math.BigDecimal;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Collection;
import java.util.Date;

public class Scraper {

    public static void main(String[] args) {
        String content = null;
        Element craigslistPage = null;
        try {
            craigslistPage = Jsoup.connect("https://sfbay.craigslist.org/d/apts-housing-for-rent/search/apa").get();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Unsuccessful http request to get craigslist listings.");
        }

        ScraperConfig config = makeHardCodeScraperConfig();

        Collection<Listing> listings = parseCraigslistPage(craigslistPage, config);

        int num = (listings == null ? 0 : listings.size());

        System.out.println("Retrieved " + (num == 1 ? "listing" : "listings") + ".");
        for (Listing current : listings) {
            System.out.println("");
            System.out.println(current);
        }
    }

    private static ScraperConfig makeHardCodeScraperConfig() {
        ScraperConfig ret = new ScraperConfig();

        Date lastSeen = null;
        try {
            lastSeen = new SimpleDateFormat("yyyy/MM/dd").parse("2018/12/19");
        } catch (ParseException e) {
            System.out.println("Unable to parse date: " + e);
        }
        ret.setLastSeen(lastSeen);

        ret.setMinPrice(new BigDecimal("800"));
        ret.setMaxPrice(new BigDecimal("1800"));
        ret.setMinBedrooms(0);
        ret.setMaxBedrooms(1);

        ret.setMaxToFetch(500);

        return ret;
    }

    public static Collection<Listing> parseCraigslistPage(Element craigslistPage, ScraperConfig config) {
        for (Element listing : craigslistPage.getElementsByClass("result-row")) {
            
        }
    }
}