#Include <Rufaydium>

OnExit("Sair")

Sair(ExitReason, ExitCode){
	WinGet LhWnd, List, % "ahk_exe " chrome.exe
	Loop, %LhWnd%
		PostMessage, 0x112, 0xF060,,, % "ahk_id " LhWnd%A_Index%
	Chrome.QuitAllSessions() ; close all session
	Chrome.Driver.Exit() ; then exits driver
	OutputDebug, Script finalizado
}

<^y::
	Chrome := new Rufaydium("chromedriver.exe")
	Page := Chrome.NewSession()
	page.navigate("https://app.acessorias.com/index.php")

	Input_email := Page.getElementsbyXpath("//*[@id='site-corpo']/section[1]/div/form/div[1]/div[1]/input")[0].value := "rafael@nexxoempresarial.com"
	Send, {Tab}
	Input_Senha := Page.getElementsbyXpath("//*[@id='site-corpo']/section[1]/div/form/div[1]/div[2]/input")[0].value := "Nexxo123@!"
	Sleep, 1000
	page.getElementsByXpath("/html/body/main/section[1]/div/form/div[2]/button")[0].click()
	Sleep, 4000
	page.getElementsbyXpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/ul/li[4]/a")[0].click()
	Sleep, 5000
	page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[3]/div[1]/input[1]")[0].value := "03/2023"
	page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[3]/div[1]/input[2]")[0].value := "03/2023"

	; page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[3]/div[1]/input[1]")[0].value := "04/2023"
	; page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[3]/div[1]/input[2]")[0].value := "04/2023"
	Sleep, 5000
	page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/button")[0].click()
	page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div/a[4]/i")[0].click()
	page.getElementsbyXpath("/html/body/div[2]/div[2]/div[2]/div/div/form/div[2]/button[1]")[0].click()
return

<^.::
ExitApp
