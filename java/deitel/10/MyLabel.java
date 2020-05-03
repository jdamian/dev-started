import java.awt.*;
import java.applet.*;

public class MyLabel extends Applet {
    private Font f;
    private Label noLabel, textLabel;

    public void init() {
        f = new Font("Courier", Font.BOLD,14);
        noLabel = new Label();
        textLabel = new Label("Este texto solo se lee");
        textLabel.setFont(f);

        add(noLabel);
        add(textLabel);

        
    }
}