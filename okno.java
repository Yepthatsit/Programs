package cookie_clicker;

import java.awt.Color;
import java.awt.Cursor;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class okno implements ActionListener {
    int score = 0;
    JLabel akcja = new JLabel("wynik = 0");
    JFrame ramka = new JFrame("cookie clicker");
    ImageIcon icon = new ImageIcon(getClass().getResource("cisatko.png"));
    JButton cookie = new JButton(icon);
    JButton cursor1 = new JButton("kursor 1");
    JButton cursor2 = new JButton("domyślny");
    public void inicjalizacja(){
        ramka.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ramka.setSize(1000,1000);
        ramka.setVisible(true);
        ramka.setLayout(null);
        ramka.getContentPane().setBackground(Color.BLUE);
        cookie.setBounds(400,400,200,200);
        cursor1.setBounds(800, 500, 100, 40);
        cursor2.setBounds(800, 550, 100, 40);
        cursor1.addActionListener(this);
        cursor2.addActionListener(this);
        cookie.addActionListener(this);
        cursor1.setEnabled(false);
        ramka.add(cookie);
        ramka.add(cursor1);
        ramka.add(cursor2);
        akcja.setBounds(800, 400 , 300 ,100 );
        akcja.setFont(new Font(null ,Font.PLAIN, 25));
        ramka.add(akcja);
        akcja.setVisible(true);
        akcja.setForeground(Color.RED);
        ramka.setCursor(new Cursor(Cursor.HAND_CURSOR));
    }
    @Override
    public void actionPerformed(ActionEvent click) {
        if(click.getSource() == cookie ){
        score += 1 ;
        akcja.setText("wynik = " + String.valueOf(score));
        }
        if (score == 10){
            cursor1.setEnabled(true);
            
        }
        if (click.getSource() == cursor1){
            ramka.setCursor(new Cursor(Cursor.CROSSHAIR_CURSOR));
        }
        if (click.getSource() == cursor2) {
            ramka.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
            
        }
        throw new UnsupportedOperationException("Unimplemented method 'actionPerformed'");
    }
}