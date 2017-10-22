package rhd.craig_app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class ListingsController {

    @RequestMapping("/listings")
    public String greeting(@RequestParam(value="num", required=false, defaultValue=10) int num,
                           @RequestParam(value="fromTs", required=false, defaultValue=0) long ts,
                           Model model) {
        model.addAttribute("name", name);
        return "greeting";
    }

}
