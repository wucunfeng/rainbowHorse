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

    @GetMapping("/index/registered")
    public void registered()
    {

    }

    /**
     * 登录
     */
    @GetMapping("/index/login")
    public void login()
    {
    }
}
