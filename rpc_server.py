


#Server Side

from xmlrpc.server import SimpleXMLRPCServer
text='''import java.util.Scanner;
import java.lang.Exception;


class InsufficientFundsException extends Exception {
    public InsufficientFundsException()
    {
        // Call constructor of parent Exception
        super();
    }
}
class Accoount
{
    private double balance;
    public void initiate(double initialBalance)
    {
        balance = initialBalance;
    }
    public void deposit(double amount)
    {
        balance = balance + amount;
    }
    public void withdraw(double amount)
    {
        try
        {
            if(balance < amount)
            {
                throw new InsufficientFundsException();
            }
            else
            {
                balance = balance - amount;
                System.out.println("\nAmount debited");
                System.out.println("Current Bank Balance = "+balance);
            }
        }
        catch(InsufficientFundsException e)
        {
            System.out.println("\nInsufficient Funds !");
        }
    }
    public double getBalance()
    {
        return balance;
    }
}

class BankAccount{
    public static void main(String[] args){
        Scanner input= new Scanner(System.in);
        Accoount acc = new Accoount();
        acc.initiate(10000);
        int opt=0;
        while(opt<4){
            System.out.println("\nBank Simulator\n");
            System.out.println("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit");
            System.out.print("Enter your choice: ");
            opt = input.nextInt();
            if(opt>4){
                System.out.println("Wrong option...");
            }
            else if(opt==1){
                System.out.print("Enter amount to deposit: ");
                double amount = input.nextDouble();
                acc.deposit(amount);
            }
            else if(opt==2){
                System.out.print("Enter amount to withdraw: ");
                double amount = input.nextDouble();
                acc.withdraw(amount);
            }
            else if(opt==3){
                System.out.println("\nBalance: "+acc.getBalance());
            }
            else if(opt==4){
                System.out.println("Thank you for using our service...");
            }
            

        }
    }
}'''
def code():
    return text

server=SimpleXMLRPCServer(("localhost",3010))
server.register_function(code)
server.serve_forever()
