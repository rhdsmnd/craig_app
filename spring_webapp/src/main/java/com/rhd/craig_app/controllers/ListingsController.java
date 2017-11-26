package rhd.craig_app.controllers;

import rhd.craig_app.domain.Listing;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class ListingsController {

    @RequestMapping("/listings")
    public Listing getListings(@RequestParam(value="startTs", required=false, defaultValue="0") String startTs) {
        Long parsedStartTs;
        try {
            parsedStartTs = Long.parseLong(startTs);
        } catch (NumberFormatException e) {
            return null;
        }
        if (parsedStartTs < 0) {
            return null;
        }

        Listing ret = new Listing();

        return ret;
    }

}