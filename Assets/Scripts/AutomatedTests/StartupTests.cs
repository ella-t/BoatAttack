using System.Collections;
using System.Collections.Generic;
using BoatAttack.UI;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;

[Category("BatchmodeTest")]
public class StartupTests
{
    
    [OneTimeSetUp]
    public void LoadInitialScene()
    {
        SceneManager.LoadScene("main_menu");
    }

    [Test, Order(1)]
    public void LoadMainScene()
    {
        Debug.Log("Loading main scene");
        switch(Application.platform) 
        {
            case RuntimePlatform.WindowsEditor:
            case RuntimePlatform.OSXEditor:
                Debug.Log("Platform=Playmode");
                break;
            case RuntimePlatform.WindowsPlayer:
                Debug.Log("Platform=Windows");
                break;
            case RuntimePlatform.Android:
                Debug.Log("Platform=Android");
                break;
        }
    }

    [UnityTest, Order(2)]
    public IEnumerator WaitForMainMenu()
    {
        yield return new WaitUntil(() => SceneManager.GetActiveScene().name == "main_menu");
    }

    [Test, Order(3)]
    public void StartNewGame()
    {
        MainMenuHelper menu = GameObject.FindWithTag("mainMenu").GetComponent<MainMenuHelper>();
        menu.SetupSpectatorGame();
        menu.StartRace();
    }

    [UnityTest, Order(4)]
    public IEnumerator WaitForIngame()
    {
        yield return new WaitUntil(() => SceneManager.GetActiveScene().name == "level_Island");
    }

    [UnityTest, Order(5)]
    public IEnumerator RunIngame()
    {
        yield return new WaitForSeconds(5);
    }

}
