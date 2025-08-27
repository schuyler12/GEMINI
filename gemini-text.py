import google.generativeai as genai

query = input("Enter your query: ").lower()
if query != "none":
            genai.configure(api_key="GOOGLE GEMINI API KEY HERE")
            model = genai.GenerativeModel("gemini-2.0-flash-lite") #please check the available models of gemini
            response = model.generate_content(f"Sir : {query}")

            if response.text:
                response_text = str(response.text).strip()
                print(f"NAVIDS: {response_text}")
            else:
                raise Exception("Empty response from Gemini")
            
                    