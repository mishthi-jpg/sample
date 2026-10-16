import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-gray-900">
         <h1 className="text-blue-700 align-center place-content-between p-4 font-mono font-bold text-6xl">FILL THE FORM</h1>
      <main className="flex w-50% h-50% flex-col items-center justify-between py-16 px-16 bg-white dark:bg-gray-800/60 backdrop-blur-xl sm:items-start sm:rounded-lg sm:border sm:border-gray-300 sm:shadow-2xl sm:dark:border-gray-700">
        <div className="flex flex-col items-center gap-6 text-center sm:items-start sm:text-left">
          <form className="flex w-full max-w-md flex-col gap-4 mt-6" action="/api/submit" method="POST">
            <label htmlFor="name">Name:</label>
            <input type="text" className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500" id="name" name="name" required />
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" className="lowercase border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500" required />
            <label htmlFor="message">Message:</label>
            <textarea id="message" name="message" rows={4} cols={50} className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500" required />
            <button type="submit" className="w-1/2 self-center rounded-4xl bg-blue-700 px-4 py-2 font-bold text-white hover:bg-blue-900 shadow-md transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
               <input type="submit"  value="Submit" />
            </button>
           
          </form>
          
        </div>
       
      </main>
    </div>
  );
}
