from orchestrator import Orchestrator




orchestrator = Orchestrator(model='gemini-3-flash-preview', client='google')

orchestrator.execute("How is situation in south america", "no articles")
