import React, { useState } from "react";
// import demoImage from "./demo.png";

import axios from "axios";

const Home = () => {
  const [text, setText] = useState("");
  const [img, setImg] = useState("");
  const [loading, setLoading] = useState(false);
  function generate() {
    setLoading(true);
    axios
      .post("./api/index", {
        text
      })
      .then(res => {
        setImg(res.data);
        setLoading(false);
      });
  }
  const ImageSrc = img ? `data:image/png;base64,${img}` : "/demo.png";
  return (
    <div className="container">
      <div className="tool">
        <h1 className="title">ZZKIA</h1>
        <h2 className="desc">诺基亚短信图片生成器</h2>
        <div className="input">
          <input
            className="text"
            placeholder="输入您想生成的短信文字"
            type="text"
            value={text}
            onChange={e => setText(e.target.value)}
          />
        </div>
        <div className="generate-box">
          <button className="generate" disabled={loading} onClick={generate}>
            {loading ? "生成中" : "生成"}
          </button>
        </div>
      </div>

      <div className="image-box">
        <img className="image" src={ImageSrc} alt="zzkia" />
      </div>

      <style jsx global>{`
        body {
          margin: 0;
          font-family: "Roboto", Arial, sans-serif;
          padding-top: 30px;
          padding-bottom: 40px;
          background: #f5efef;
        }
        .generate-box {
          text-align: center;
          margin-top: 10px;
        }
        .generate {
          background: transparent;
          color: rgba(0, 0, 0, 0.55);
          border-radius: 5px;
          padding: 10px 20px;
          font-size: 0.7rem;
          font-weight: 500;
          transition: all 0.5s;
        }

        .generate {
          border: 1px solid #0288d1;
        }

        .generate:hover {
          background: #0288d1;
          color: white;
        }
        .image-box {
          text-align: center;
          margin: 30px 0;
        }
        .image {
          height: 500px;
        }
        html {
          box-sizing: border-box;
        }

        button {
          cursor: pointer;
          outline: none;
          border: none;
        }

        * {
          box-sizing: inherit;
        }

        ul {
          padding: 0;
          margin: 0;
          list-style: none;
        }

        .container {
          margin: 0 auto;
          max-width: 1200px;
          padding: 0 100px;
        }

        .title {
          font-size: 1.7rem;
          color: #666666;
        }

        .desc {
          font-size: 0.9rem;
          color: #9bc788;
        }

        .tool {
          text-align: center;
          padding-bottom: 20px;
          border-bottom: 1px solid rgba(0, 0, 0, 0.14);
        }

        .tool .text {
          border: none;
          width: 100%;
          background: #fefefe;
          border-radius: 40px;
          box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
          outline: none;
          font-size: 13px;
          color: #5a6674;
          padding: 10px 15px;
        }

        .input {
          position: relative;
          width: 300px;
          height: 38px;
          margin: 0 auto;
        }

        .input #visit {
          position: absolute;
          right: 0;
          height: 50px;
          width: 50px;
          top: -7px;
          transition: all 0.3s;
        }

        .visit > svg {
          height: 100%;
          width: 100%;
          fill: #e57373;
        }

        .visit:hover {
          transform: rotate(90deg);
        }

        .block-box {
          position: relative;
          text-align: center;
          width: 600px;
          margin: 0 auto;
          padding-top: 20px;
          padding-bottom: 40px;
          border-bottom: 1px solid rgba(0, 0, 0, 0.14);
        }

        .block .page {
          font-size: 1.6rem;
        }

        .history-message {
          text-align: center;
        }

        @media screen and (max-width: 768px) {
          .container {
            padding: 0;
            width: 100%;
          }
          .block-box {
            width: 100%;
          }
          .block-box .block {
            width: 50%;
            height: 50vw;
          }
          #message-pool {
            max-width: calc(100vw - 30px);
          }
        }
      `}</style>
    </div>
  );
};

export default Home;
