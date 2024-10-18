<template>
    <div class="self-intro">
        <div class="intro-header">
            <img src="@/assets/picture.png" alt="Owen" class="profile-photo" />
            <h1>嗨囉 😊 我是 曾證蒼</h1>
            <div class="social-links">
                <a href="https://github.com/owen-0513" target="_blank" class="social-icon">
                    <i class="fab fa-github"></i>
                </a>
            </div>
        </div>

        <div class="intro-content">
            <h2>個人資料</h2>
            <p><strong>出生年月：</strong>1992年</p>
            <p><strong>教育背景：</strong>明新科技大學</p>

            <h2>職業目標</h2>
            <p>
                致力於在科技產業中，通過軟體開發與測試技能推動創新和效率提升，持續為公司和團隊創造價值。
            </p>

            <h2>專業技能</h2>
            <ul>
                <li>熟練掌握 C++、Java、Python、JavaScript、HTML 和 CSS。</li>
                <li>深入了解 Flash、eMMC、SD 等存儲技術，以及相關的命令分析和訊號量測技術。</li>
                <li>擁有豐富的軟體開發和自動化測試經驗，專業於系統整合和性能優化。</li>
                <li>出色的問題解決能力，能快速定位並修復 Bug。</li>
                <li>擅長分析數據並制定有效的測試方案，確保軟體質量符合產業標準。</li>
            </ul>

            <h2>工作經歷</h2>

            <h3>JAVA 高級軟體工程師</h3>
            <ul>
                <li>負責客製化軟體開發和系統整合，專注於提升用戶體驗和系統性能。</li>
                <li>參與系統故障排除，確保項目按時交付，並達到或超越預期效果。</li>
            </ul>

            <h3>軟體工程師</h3>
            <ul>
                <li>參與軟體開發項目，從系統設計到實施，包括前端畫面設計和系統更新。</li>
                <li>負責系統維護和升級，保證系統的穩定運行和持續改進。</li>
            </ul>

            <h3>測試工程師</h3>
            <ul>
                <li>主導遊戲軟體的測試計畫設計，開發詳細的測試案例，並監控測試進度。</li>
                <li>執行質量控制，確保軟體符合行業標準，並提升遊戲的穩定性和使用者體驗。</li>
            </ul>

            <h3>助理工程師</h3>
            <ul>
                <li>負責分析和量測 Flash、eMMC、SD 等存儲技術產品的命令和訊號。</li>
                <li>參與 PCIE 和 SATA 新產品開發，專注於相容性測試和問題排查。</li>
                <li>提交詳盡的測試報告，提供有價值的改進建議，顯著優化產品性能。</li>
            </ul>

            <h2>未來規劃</h2>
            <p>
                計劃進一步深入人工智慧和機器學習領域，探索 AI 技術在軟體開發和測試中的應用。
                特別是將自動化測試、數據分析和使用者體驗結合，提升軟體品質。
                通過不斷學習和實踐，期望成為該領域的專家，為未來的科技發展貢獻更多價值。
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SelfIntroduction',
};
</script>

<style scoped>
.self-intro {
    text-align: center;
    padding: 80px 20px;
    background-color: white;
    color: black;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}

.intro-header {
    margin-bottom: 40px;
}

.profile-photo {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

h2 {
    font-size: 28px;
    margin-top: 40px;
    margin-bottom: 20px;
}

h3 {
    font-size: 22px;
    margin-bottom: 10px;
}

.social-links {
    margin-top: 20px;
}

.social-icon {
    font-size: 36px;
    color: black;
    margin: 0 10px;
    transition: color 0.3s, transform 0.3s;
}

.social-icon:hover {
    color: #007bff;
    transform: scale(1.1);
}

.intro-content {
    max-width: 800px;
    font-size: 18px;
    line-height: 1.8;
    text-align: left;
}

ul {
    list-style-type: disc;
    margin-left: 20px;
}

p,
ul {
    margin-bottom: 20px;
}
</style>
