import java.util.Scanner;
public class salary {
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        System.out.println(input.nextLine());
        int salary=input.nextInt();

        if(salary>25000){
            salary=salary+5000;
            System.out.println("Congratulations! Your salary was reach of the range So you will provide the five thousand bonus by the company= " + salary);
        }
        else{
            salary=salary+2500;
            System.out.println("Sorry! your salary is minimum so you have not provide the bonus by the company="+salary);
        }
       // System.out.println("Congratulations! Your salary was reach of the range So you will provide the five thousand bonus by the company= " + salary);
    }
   // System.out.println("Congratulations! Your salary was reach of the range So you will provide the five thousand bonus by the company= " + salary);
}
