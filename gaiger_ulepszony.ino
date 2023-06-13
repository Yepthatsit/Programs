#include <LiquidCrystal_I2C.h>
int czytnik = 3;
int start;
int aktualny;
int rozp;
int cpm [60];
int rpm;
LiquidCrystal_I2C lcd(0x27, 16 , 2); // zdefiniowanie wyświetlacza
void setup() {
  // put your setup code here, to run once:
  pinMode(czytnik,INPUT);
  attachInterrupt(digitalPinToInterrupt(czytnik), licznik, RISING);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Pierwszy pomiar");

}

void loop() {
  // put your main code here, to run repeatedly:
  start=millis();
  aktualny = millis();


  while((aktualny - start) <= 1000){ //pętla czasomierz
    aktualny = millis();
  }
  // wyświetla rozpady na 1 sekund
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(rozp);
  //aktualizuje liste 
  for (int i =59; i>=1; i-- ){
    cpm[i] = cpm[i-1];
  }
  cpm[0]= rozp;
  rozp= 0 ;
  for (int j=0; j<60; j++){
    rpm += cpm[j];
  }
  //wyświetla rozpady na minutę
  lcd.setCursor(13, 0);
  lcd.print("CPS");
  lcd.setCursor(0, 1);
  lcd.print(rpm);
  lcd.setCursor(13, 1);
  lcd.print("CPM");
  rpm = 0;
}
void licznik(){
     rozp= rozp + 1 ;
     

     
     

}