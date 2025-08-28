// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-lectures",
          title: "lectures",
          description: "강의자료 collection",
          section: "Navigation",
          handler: () => {
            window.location.href = "/lectures/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "Youngung Jeong&#39;s CV",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-people",
          title: "people",
          description: "Current members of the lab",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "dropdown-bookshelf",
              title: "bookshelf",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/books/";
              },
            },{id: "dropdown-blog",
              title: "blog",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/blog/";
              },
            },{id: "post-nist-교환-학생-소식",
        
          title: "NIST 교환 학생 소식",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/NIST_JSL/";
          
        },
      },{id: "post-2025-july-numisheet-학회-참석-및-발표",
        
          title: "2025 July, NUMISHEET 학회 참석 및 발표",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/numisheet/";
          
        },
      },{id: "post-2024-july-lanl-방문",
        
          title: "2024 July, LANL 방문",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/LANL-visit/";
          
        },
      },{id: "post-a-post-with-tabs",
        
          title: "a post with tabs",
        
        description: "this is what included tabs in a post could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/tabs/";
          
        },
      },{id: "post-a-post-with-typograms",
        
          title: "a post with typograms",
        
        description: "this is what included typograms code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/typograms/";
          
        },
      },{id: "post-a-post-that-can-be-cited",
        
          title: "a post that can be cited",
        
        description: "this is what a post that can be cited looks like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/post-citation/";
          
        },
      },{id: "post-a-post-with-pseudo-code",
        
          title: "a post with pseudo code",
        
        description: "this is what included pseudo code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/pseudocode/";
          
        },
      },{id: "post-a-post-with-code-diff",
        
          title: "a post with code diff",
        
        description: "this is how you can display code diffs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/code-diff/";
          
        },
      },{id: "post-a-post-with-advanced-image-components",
        
          title: "a post with advanced image components",
        
        description: "this is what advanced image components could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/advanced-images/";
          
        },
      },{id: "post-a-post-with-vega-lite",
        
          title: "a post with vega lite",
        
        description: "this is what included vega lite code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/vega-lite/";
          
        },
      },{id: "post-a-post-with-geojson",
        
          title: "a post with geojson",
        
        description: "this is what included geojson code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/geojson-map/";
          
        },
      },{id: "post-a-post-with-echarts",
        
          title: "a post with echarts",
        
        description: "this is what included echarts code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/echarts/";
          
        },
      },{id: "post-a-post-with-chart-js",
        
          title: "a post with chart.js",
        
        description: "this is what included chart.js code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/chartjs/";
          
        },
      },{id: "post-a-post-with-tikzjax",
        
          title: "a post with TikZJax",
        
        description: "this is what included TikZ code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/tikzjax/";
          
        },
      },{id: "post-2023-september-ictp",
        
          title: "2023 September ICTP",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/ictp/";
          
        },
      },{id: "post-a-post-with-bibliography",
        
          title: "a post with bibliography",
        
        description: "an example of a blog post with bibliography",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/post-bibliography/";
          
        },
      },{id: "post-a-post-with-jupyter-notebook",
        
          title: "a post with jupyter notebook",
        
        description: "an example of a blog post with jupyter notebook",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/jupyter-notebook/";
          
        },
      },{id: "post-a-post-with-custom-blockquotes",
        
          title: "a post with custom blockquotes",
        
        description: "an example of a blog post with custom blockquotes",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/custom-blockquotes/";
          
        },
      },{id: "post-a-post-with-table-of-contents-on-a-sidebar",
        
          title: "a post with table of contents on a sidebar",
        
        description: "an example of a blog post with table of contents on a sidebar",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/sidebar-table-of-contents/";
          
        },
      },{id: "post-a-post-with-audios",
        
          title: "a post with audios",
        
        description: "this is what included audios could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/audios/";
          
        },
      },{id: "post-a-post-with-videos",
        
          title: "a post with videos",
        
        description: "this is what included videos could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/videos/";
          
        },
      },{id: "post-displaying-beautiful-tables-with-bootstrap-tables",
        
          title: "displaying beautiful tables with Bootstrap Tables",
        
        description: "an example of how to use Bootstrap Tables",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/tables/";
          
        },
      },{id: "post-a-post-with-giscus-comments",
        
          title: "a post with giscus comments",
        
        description: "an example of a blog post with giscus comments",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/giscus-comments/";
          
        },
      },{id: "post-u-draw-bending-c-rail-fea-with-devpsc-fe",
        
          title: "U-draw bending, C-rail FEA with dEVPSC-FE",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/dEVPSC-FE-Udraw/";
          
        },
      },{id: "post-a-post-with-diagrams",
        
          title: "a post with diagrams",
        
        description: "an example of a blog post with diagrams",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2021/diagrams/";
          
        },
      },{id: "post-a-distill-style-blog-post",
        
          title: "a distill-style blog post",
        
        description: "an example of a distill-style blog post and main elements",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2021/distill/";
          
        },
      },{id: "post-a-post-with-image-galleries",
        
          title: "a post with image galleries",
        
        description: "this is what included image galleries could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2020/photo-gallery/";
          
        },
      },{id: "post-a-post-with-plotly-js",
        
          title: "a post with plotly.js",
        
        description: "this is what included plotly.js code could look like",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2020/plotly/";
          
        },
      },{id: "post-집합조직-확산사업-워크샵-참석-및-강연",
        
          title: "집합조직 확산사업 워크샵 참석 및 강연",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/textureworkshop/";
          
        },
      },{id: "post-numisheet-2018",
        
          title: "Numisheet 2018",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/Numisheet2018/";
          
        },
      },{id: "post-dr-carlos-tome-visits-mml-cwnu",
        
          title: "Dr. Carlos Tome visits MML@CWNU",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/Carlos/";
          
        },
      },{id: "post-guests-from-kmutnb",
        
          title: "Guests from KMUTNB",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/Thai/";
          
        },
      },{id: "post-전산재료과학-모임",
        
          title: "전산재료과학 모임",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/meeting/";
          
        },
      },{id: "post-korea-japan-neutron-user-meeting",
        
          title: "Korea-Japan Neutron User Meeting",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/KJ/";
          
        },
      },{id: "post-final-성적-공지",
        
          title: "Final 성적 공지",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2018/Notice/";
          
        },
      },{id: "post-학회-참석",
        
          title: "학회 참석",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2017/KIMM/";
          
        },
      },{id: "post-새-구성원",
        
          title: "새 구성원",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2017/Newmembers/";
          
        },
      },{id: "post-iddrg-2017-참석-및-freiberg-방문",
        
          title: "IDDRG 2017 참석 및 Freiberg 방문",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2017/Germany/";
          
        },
      },{id: "post-첫여름방학",
        
          title: "첫여름방학",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2017/first-summer-break/";
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "lectures-데이터-재료과학",
          title: '데이터 재료과학',
          description: "데이터 분석/해석 및 시각화(그래프) 등 기초 컴퓨터 활용 능력",
          section: "Lectures",handler: () => {
              window.location.href = "/lectures/1_2_data_mse/";
            },},{id: "lectures-수치해석",
          title: '수치해석',
          description: "재료공학도를 위한 수치해석",
          section: "Lectures",handler: () => {
              window.location.href = "/lectures/2_1_numerical_analysis/";
            },},{id: "lectures-이동현상",
          title: '이동현상',
          description: "",
          section: "Lectures",handler: () => {
              window.location.href = "/lectures/2_2_transport/";
            },},{id: "lectures-소성가공",
          title: '소성가공',
          description: "",
          section: "Lectures",handler: () => {
              window.location.href = "/lectures/3_1_metal_plasticity/";
            },},{id: "news-홈페이지를-개편하고-있습니다-sparkles-smile",
          title: '홈페이지를 개편하고 있습니다 :sparkles: :smile:',
          description: "",
          section: "News",},{id: "projects-개인연구-중견",
          title: '개인연구(중견)',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/midcarrier/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%79%6A%65%6F%6E%67@%63%68%61%6E%67%77%6F%6E.%61%63.%6B%72", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=ANercDoAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
