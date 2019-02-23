package Page;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    /**
     *显示页面主页
     */
    @GetMapping("/index")
    public String Index()
    {
        return "index";
    }
}
